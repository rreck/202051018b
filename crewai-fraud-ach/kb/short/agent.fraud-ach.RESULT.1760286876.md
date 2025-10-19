```json
{
  "id": "45e1ba17952ce7eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286876,
  "host_pid": "9e6742732c60:1",
  "hash": "d242df7d22c8bbbbb363b50455800f90e41c3e940cdccd8786554db2b31136be",
  "cid": "QmV1d242df7d22c8bbbbb363b50455800f90e41c3e94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286876,
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
      "evaluated_at": 1760286876
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
  "sig": "009826897355a3e1bb0f031591cb646a3c477744aca697a2c0f0aeb92a1fa203"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000039663431
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 39, 'first_seen': 1760285764, 'matching_hash': '33f644fe289ea89d'}}}