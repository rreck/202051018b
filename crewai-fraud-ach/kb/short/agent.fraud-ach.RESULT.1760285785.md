```json
{
  "id": "8b554d4bdad6c2bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285785,
  "host_pid": "9e6742732c60:1",
  "hash": "29f310c24739a3412b38fd90aa86bc92c55a1750052cd52939ea9e82bd52bd7e",
  "cid": "QmV129f310c24739a3412b38fd90aa86bc92c55a1750",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285785,
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
      "evaluated_at": 1760285785
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
  "sig": "48386276ab42b82e12386b211bd03b079f1526dece6880490a879196a2095b57"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105151957108
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 1, 'first_seen': 1760285765, 'matching_hash': 'c64e753eaec43197'}}}