```json
{
  "id": "c37c0b4fd36c9041",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286424,
  "host_pid": "9e6742732c60:1",
  "hash": "6c180bd7851c472bfd73b186f31ef566011c83cba493be5e6c76aea8ee7b4687",
  "cid": "QmV16c180bd7851c472bfd73b186f31ef566011c83cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286424,
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
      "evaluated_at": 1760286424
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
  "sig": "e5bde43dcc53d31643915a2b93be9588b9a448e051ed566ba21faccfcbe62084"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591752071
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285763, 'matching_hash': 'afb8628b94bcbefe'}}}