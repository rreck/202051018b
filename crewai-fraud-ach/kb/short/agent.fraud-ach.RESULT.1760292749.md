```json
{
  "id": "aaaa330887274d02",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292749,
  "host_pid": "9e6742732c60:1",
  "hash": "22ee97e368c81fdaa36da910d82938b6af778f6d17abdb3ba9b09351b5a589e6",
  "cid": "QmV122ee97e368c81fdaa36da910d82938b6af778f6d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292749,
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
      "evaluated_at": 1760292749
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
  "sig": "ae58e8f246aa64c52d44aca40e4ceccef4760db2353a15d0c9fadec910e52df9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037779899
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 83849508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '90378a324202fffb'}}}