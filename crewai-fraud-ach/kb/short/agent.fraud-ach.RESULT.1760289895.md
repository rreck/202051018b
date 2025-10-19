```json
{
  "id": "abaeb2935d0f78fc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289895,
  "host_pid": "9e6742732c60:1",
  "hash": "4686e6e958edd21129f67a29e94d9dd28d02d34845133d9761d0175d9b14b7ea",
  "cid": "QmV14686e6e958edd21129f67a29e94d9dd28d02d348",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289895,
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
      "evaluated_at": 1760289895
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
  "sig": "87a0d36887b8b41c9c5f2f19512f0f47015914234b7bd2cf3c5567854a618168"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000028364021
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 136, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 135, 'first_seen': 1760285763, 'matching_hash': 'f023f2061dd68ffa'}}}een': 1760285764, 'matching_hash': 'a3ad727f5ed38962'}}}