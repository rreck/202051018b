```json
{
  "id": "dfa7643fd22761b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286248,
  "host_pid": "9e6742732c60:1",
  "hash": "517bcff658a70d626cb0139c51b605c701cd1c6265151fb5b7ebbbc5d485f46e",
  "cid": "QmV1517bcff658a70d626cb0139c51b605c701cd1c62",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286248,
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
      "evaluated_at": 1760286248
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
  "sig": "46e8344afbc6c250ecae8062fcfcc7547495c9a882faefd1cf954523d72e92c9"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000244947778
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 18, 'first_seen': 1760285763, 'matching_hash': '9c8f06e6a18eec99'}}}