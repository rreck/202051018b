```json
{
  "id": "15866ea55d6d5519",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286988,
  "host_pid": "9e6742732c60:1",
  "hash": "cc1d560cd7c6f45100f07f147b15506f3dfb64e93bab8bb1f519341dcc7d9dd3",
  "cid": "QmV1cc1d560cd7c6f45100f07f147b15506f3dfb64e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286988,
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
      "evaluated_at": 1760286988
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
  "sig": "41f99e53e7a859edf979b94ea1e2967e6a1a366e6f6888097d991b1c73c63183"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000037423947
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 43, 'first_seen': 1760285763, 'matching_hash': '5528b0ca47a44e30'}}}