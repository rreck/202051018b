```json
{
  "id": "e5a88836b4a389af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286072,
  "host_pid": "9e6742732c60:1",
  "hash": "b4595cd629dc8433622c9f4aedacf9365222935c00f3349382c01492068f2806",
  "cid": "QmV1b4595cd629dc8433622c9f4aedacf9365222935c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286072,
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
      "evaluated_at": 1760286072
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
  "sig": "d161b9026890cb28852f96229835fa08b2eb70e729ed478dd500cc25c4e52851"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201463882943
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': '0eb18222520b1d39'}}}