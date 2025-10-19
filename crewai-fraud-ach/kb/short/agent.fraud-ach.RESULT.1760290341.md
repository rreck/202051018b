```json
{
  "id": "443c1da43cc062bf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290341,
  "host_pid": "9e6742732c60:1",
  "hash": "a4d02a2d5222ff969c2ddff3c976f911d6844ac2bdd6daaafea63fe1425565f6",
  "cid": "QmV1a4d02a2d5222ff969c2ddff3c976f911d6844ac2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290341,
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
      "evaluated_at": 1760290341
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
  "sig": "71b925127a80bfe58afced05be716ae5cbe3dd34c906723ae555dba4e403ba34"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591682020
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 43068740, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285763, 'matching_hash': '594333c81206e179'}}}