```json
{
  "id": "52ee26a7bb82baa5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287873,
  "host_pid": "9e6742732c60:1",
  "hash": "313c05bb8a53a96ae30c10bca5bfc4f9b4d4eb5c201085e59909d01318965722",
  "cid": "QmV1313c05bb8a53a96ae30c10bca5bfc4f9b4d4eb5c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287873,
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
      "evaluated_at": 1760287873
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
  "sig": "ba7b9ab3f775d53462ceb961d5aeff8e6fab0384ed94186943f629f8dc56cce0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243386632
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 75, 'threshold': 50, 'total_amount': 16635375, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 74, 'first_seen': 1760285763, 'matching_hash': 'a6aa6f7765b452ca'}}}}}