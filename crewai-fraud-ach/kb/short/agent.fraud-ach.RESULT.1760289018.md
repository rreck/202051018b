```json
{
  "id": "0e656b2af080d55d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289018,
  "host_pid": "9e6742732c60:1",
  "hash": "21bdeffe06de3feb7682c7eae3cc37afa8b5116b286a405bda721f78400553fa",
  "cid": "QmV121bdeffe06de3feb7682c7eae3cc37afa8b5116b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289018,
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
      "evaluated_at": 1760289018
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
  "sig": "4d7ab4fa8c911de99275d12b1b450e5b2acf43738df0ffbe002acbf0058e9f01"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154361187
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 27750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285764, 'matching_hash': 'a57b8c5e7960514a'}}}