```json
{
  "id": "5dd8726a25d64789",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286582,
  "host_pid": "9e6742732c60:1",
  "hash": "8bd17d955d75212be97050f83a1cc61682396ff80b0b8af1377125b3da269324",
  "cid": "QmV18bd17d955d75212be97050f83a1cc61682396ff8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286582,
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
      "evaluated_at": 1760286582
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
  "sig": "8a8ac2639a7d03f4df99537e81b061ec6ebdcfdc4e423bbfa0991361454cbd29"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 031201465603072
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 29, 'first_seen': 1760285763, 'matching_hash': 'e359f7b1cd5a9343'}}}