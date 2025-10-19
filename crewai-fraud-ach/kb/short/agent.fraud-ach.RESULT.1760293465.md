```json
{
  "id": "a0c50d0ab399f778",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293465,
  "host_pid": "9e6742732c60:1",
  "hash": "1ac455b4bf3ca8b4fe90c5dfb46d0af06156e0315886b70e640d29878d1fec13",
  "cid": "QmV11ac455b4bf3ca8b4fe90c5dfb46d0af06156e031",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293465,
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
      "evaluated_at": 1760293465
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
  "sig": "c9c86115dd300642a3926f83df6f3c76bd48271a6a0452e9c3c8e1b1ca65029e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153776491
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 219, 'threshold': 50, 'total_amount': 19379967, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 218, 'first_seen': 1760285763, 'matching_hash': '94746339473c09ed'}}}