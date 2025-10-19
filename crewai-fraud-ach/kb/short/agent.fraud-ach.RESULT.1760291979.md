```json
{
  "id": "c108ab4821f50e38",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291979,
  "host_pid": "9e6742732c60:1",
  "hash": "7180086aec5a37a6ccfa2da42f90a6d4b03e4d3ca457be5610088e2cba1f6d9b",
  "cid": "QmV17180086aec5a37a6ccfa2da42f90a6d4b03e4d3c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291979,
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
      "evaluated_at": 1760291979
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
  "sig": "19b4976b4caee00cdeaba57f042653cd113ce950e72c4b5d422fd8aeef6bed79"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593801655
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 67096348, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285765, 'matching_hash': '965a85028669bcfb'}}}