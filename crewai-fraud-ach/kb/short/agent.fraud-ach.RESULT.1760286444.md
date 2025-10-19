```json
{
  "id": "0c4271d504abde89",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286444,
  "host_pid": "9e6742732c60:1",
  "hash": "f022a04de077329544e32498bea0972450d675c95a466dcd8d25b48983cdfd7f",
  "cid": "QmV1f022a04de077329544e32498bea0972450d675c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286444,
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
      "evaluated_at": 1760286444
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
  "sig": "b785ad86ce46701dbbf1cc4362c9bfd087465bc2545f3de4a66fe8a7d19b0cf4"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000029386599
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}