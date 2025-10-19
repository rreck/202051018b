```json
{
  "id": "6dd17c4567d1ec75",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293089,
  "host_pid": "9e6742732c60:1",
  "hash": "44e77b7a74e48902be571a0979a53c582569cc3ee232da227645df5e51d8be43",
  "cid": "QmV144e77b7a74e48902be571a0979a53c582569cc3e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293089,
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
      "evaluated_at": 1760293089
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
  "sig": "4e226917daaea48fbe67f8ef4350d6da88b7d0ce0ad9ee873b9f248b82b4f772"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105155104424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 211, 'threshold': 50, 'total_amount': 60698792, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 210, 'first_seen': 1760285763, 'matching_hash': 'b81635ada84cf521'}}}