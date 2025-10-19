```json
{
  "id": "924018b9ed61e22f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288697,
  "host_pid": "9e6742732c60:1",
  "hash": "24f78d00543505c5ad534fe92386085b2c0441428923123834f9b98bc381274e",
  "cid": "QmV124f78d00543505c5ad534fe92386085b2c044142",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288697,
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
      "evaluated_at": 1760288697
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
  "sig": "3c0003e3cadd8d73bf9a60f7e750b50c989be8a3bc3f269233e1badb39483846"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593077739
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 27617440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285763, 'matching_hash': 'dc5b0e0c6a053908'}}}