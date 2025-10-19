```json
{
  "id": "e45a9104c72b32c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286075,
  "host_pid": "9e6742732c60:1",
  "hash": "ed72505efceb3d16609cccca0a882b754e00df259dd68e7dd47c1ebcc6b47bfd",
  "cid": "QmV1ed72505efceb3d16609cccca0a882b754e00df25",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286075,
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
      "evaluated_at": 1760286075
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
  "sig": "68cbe7b60ad5054f4613a6d7c97e9444c6a2a7c4ac301214eaa59271af101424"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009594254224
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 12, 'first_seen': 1760285765, 'matching_hash': 'a2bdc2eb52125893'}}}