```json
{
  "id": "8d713e3332d96b22",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294605,
  "host_pid": "9e6742732c60:1",
  "hash": "61240d7849bf38e59847bcd2aa231e5fa55321e2b67eb54d460f63d9684d7d23",
  "cid": "QmV161240d7849bf38e59847bcd2aa231e5fa55321e2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294605,
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
      "evaluated_at": 1760294605
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
  "sig": "f5d09e77f1edd71263334bdd6eac6763fbae8a4aaee32f83009083d4755002ea"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201461912165
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 84619679, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285763, 'matching_hash': 'd770463353c2594b'}}}}