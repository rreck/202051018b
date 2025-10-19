```json
{
  "id": "64c128335995d157",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291840,
  "host_pid": "9e6742732c60:1",
  "hash": "4c060af5f2a4ff2b43ae5db61b02be51d16deb3450d0f876997c1c9bdc2aee71",
  "cid": "QmV14c060af5f2a4ff2b43ae5db61b02be51d16deb34",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291840,
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
      "evaluated_at": 1760291840
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
  "sig": "6399dbd19545c4e1e89ed1a05a71b850f3262cd44198a8d5aeaf2d8c860daff2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240631421
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 184, 'threshold': 50, 'total_amount': 26838424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 183, 'first_seen': 1760285763, 'matching_hash': 'a12eb13bd276459e'}}}