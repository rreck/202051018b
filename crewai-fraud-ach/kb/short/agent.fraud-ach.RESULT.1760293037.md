```json
{
  "id": "b1fc9907af570e87",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293037,
  "host_pid": "9e6742732c60:1",
  "hash": "e8b76f6bc2dc0b05fb52c4e8dabdb761181fa3298d75d49a0cc6a3bdfa4fe35c",
  "cid": "QmV1e8b76f6bc2dc0b05fb52c4e8dabdb761181fa329",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293037,
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
      "evaluated_at": 1760293037
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
  "sig": "bdfde4d771b10a489a10541669929f1c49391aee0ff28ba98bffefe5db6be67a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030798175
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 286, 'threshold': 50, 'total_amount': 34060312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 285, 'first_seen': 1760284979, 'matching_hash': 'fdbb68f6e232305a'}}}