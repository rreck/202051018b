```json
{
  "id": "3865c1052101e8d8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289948,
  "host_pid": "9e6742732c60:1",
  "hash": "b9dbfd1bf2d50a4e7ecb1334e6cd9c89dd0c4ab87ebd3be89db88f92e401e381",
  "cid": "QmV1b9dbfd1bf2d50a4e7ecb1334e6cd9c89dd0c4ab8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289948,
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
      "evaluated_at": 1760289948
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
  "sig": "3a9481e56357f46a8fedb685e9d9e065fe7d769f9f6f453413ad16630e66cb15"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599118273
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 17804794, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285765, 'matching_hash': '777fe2ef7ab8cdc9'}}}