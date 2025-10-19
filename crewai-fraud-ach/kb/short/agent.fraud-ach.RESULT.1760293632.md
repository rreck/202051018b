```json
{
  "id": "77e3310420398f51",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293632,
  "host_pid": "9e6742732c60:1",
  "hash": "fe488e1cf17f3933b9da36a22949a44fec98cc69a90723ac13804a24277078ca",
  "cid": "QmV1fe488e1cf17f3933b9da36a22949a44fec98cc69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293632,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760293632
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "969364362dd25c9cab2d0d91664e7196ba9ec41cc9e6b22e2a68e69066feace5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105157316048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 55500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285764, 'matching_hash': '8f4887477877b00a'}}}