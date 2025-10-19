```json
{
  "id": "40722d7db352ff54",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292130,
  "host_pid": "9e6742732c60:1",
  "hash": "99dfdb58edb2f73d5b7d09e4334ebc2a607c028390a803762b86acfd675e720d",
  "cid": "QmV199dfdb58edb2f73d5b7d09e4334ebc2a607c0283",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292130,
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
      "evaluated_at": 1760292130
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
  "sig": "8cb3395ea9a34b7be51f22927a844220fba5992ee3bcf7ba994d897252d745eb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000033919598
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 71989619, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '1dbf667d29bdf8b7'}}}