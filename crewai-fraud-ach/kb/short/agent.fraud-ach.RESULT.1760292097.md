```json
{
  "id": "44c4d13b6fb50fae",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292097,
  "host_pid": "9e6742732c60:1",
  "hash": "d77590a07f94a9153cdeabbd78f4f5034f6e41f4461ac2affb761cbe3d8170cb",
  "cid": "QmV1d77590a07f94a9153cdeabbd78f4f5034f6e41f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292097,
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
      "evaluated_at": 1760292097
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
  "sig": "55a5b8f95c859dad072c7d22be4c716a1819b08a82fda2de92e2fc32894ecf38"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009595557022
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 190, 'threshold': 50, 'total_amount': 90436390, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 189, 'first_seen': 1760285764, 'matching_hash': '3443c05f2ecc9733'}}}