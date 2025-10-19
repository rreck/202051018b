```json
{
  "id": "d744eadcb2fc85e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289984,
  "host_pid": "9e6742732c60:1",
  "hash": "5b682a9125d6753674a9d20628dacc6e71815b59d0c6526dd514009390946181",
  "cid": "QmV15b682a9125d6753674a9d20628dacc6e71815b59",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289984,
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
      "evaluated_at": 1760289984
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
  "sig": "d574136ba36f560b5d78ff2e988dc38d555cb9fd26c40dbb32dd77f1f3ed785a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469103825
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 49926882, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285764, 'matching_hash': 'e83bf56ea8077a45'}}}