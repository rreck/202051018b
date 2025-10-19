```json
{
  "id": "6e4e3083f18869b4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291832,
  "host_pid": "9e6742732c60:1",
  "hash": "4da1e7846cdb38e85b5a7fe982015ae477cd8e2928a4a559a8705c2a74fc6aac",
  "cid": "QmV14da1e7846cdb38e85b5a7fe982015ae477cd8e29",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291832,
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
      "evaluated_at": 1760291832
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
  "sig": "475a4d883c6724e2096bfd3d57a16632a6c7f89abb348273b998ddb094940351"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242647259
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 48403776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': '186ae6e653ee56a6'}}}