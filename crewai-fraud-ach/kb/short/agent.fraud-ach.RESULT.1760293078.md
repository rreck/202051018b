```json
{
  "id": "c310eba50074daf4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293078,
  "host_pid": "9e6742732c60:1",
  "hash": "83a41a8abbafe7dfc4c7a2cf6f085e112bd75880c730fc1f06ad941ae2cd27a4",
  "cid": "QmV183a41a8abbafe7dfc4c7a2cf6f085e112bd75880",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293078,
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
      "evaluated_at": 1760293078
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
  "sig": "27f561785a859af03de761f89a8a4585d7faa8fbff33e19b9a42b046eb715d1d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460007503
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 37572981, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': '17a9441d6a1d37be'}}}