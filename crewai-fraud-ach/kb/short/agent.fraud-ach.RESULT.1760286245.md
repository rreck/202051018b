```json
{
  "id": "cc7fe4b12e23ee02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286245,
  "host_pid": "9e6742732c60:1",
  "hash": "77f77f2bf6cf8f147b790f902efa34b6f0a3832b7e41d7e046692641f2fd40ea",
  "cid": "QmV177f77f2bf6cf8f147b790f902efa34b6f0a3832b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286245,
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
      "evaluated_at": 1760286245
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
  "sig": "86635f663532108ab3e5f8e18895424270d284e0b300dd6e3e7a387f24cb0d71"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028775289
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 95, 'threshold': 50, 'total_amount': 35386835, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 94, 'first_seen': 1760284979, 'matching_hash': 'c3a7255fa6117479'}}}