```json
{
  "id": "6427049193337f95",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286196,
  "host_pid": "9e6742732c60:1",
  "hash": "0776f72b2b27eb1dc71a617b94e93a27261f428907e2e0e46b4cb4bd187f0cd8",
  "cid": "QmV10776f72b2b27eb1dc71a617b94e93a27261f4289",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286196,
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
      "evaluated_at": 1760286196
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
  "sig": "8780584bc35816bcf02126560ece13216902ecd58deb8a668317555a5aa1753b"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 16, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}