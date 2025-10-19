```json
{
  "id": "113900892ec2d073",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287346,
  "host_pid": "9e6742732c60:1",
  "hash": "77ec458b3cadde448843e4adacbf5884ef691b06b5b9327624c20cfee675332c",
  "cid": "QmV177ec458b3cadde448843e4adacbf5884ef691b06",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287346,
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
      "evaluated_at": 1760287346
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "4e2ced36e3aaa097c08628938b3458763ece6bd416b9cb8ec60ff8039e5f5753"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000031517905
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 25396407, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285763, 'matching_hash': 'e8f76fb2eb784ea5'}}}