```json
{
  "id": "f14b9cce7cb9a9a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285891,
  "host_pid": "9e6742732c60:1",
  "hash": "40df3712d1e59528c529178383732642da83bafbafee5602640efb3f5a743f23",
  "cid": "QmV140df3712d1e59528c529178383732642da83bafb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285891,
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
      "evaluated_at": 1760285891
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
  "sig": "3e027cb59b1e96c445be4a7891c22565b68defaf966476afd05695da7c343d0c"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009598660548
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 6, 'first_seen': 1760285763, 'matching_hash': '4ba6ddd8e6715c89'}}}