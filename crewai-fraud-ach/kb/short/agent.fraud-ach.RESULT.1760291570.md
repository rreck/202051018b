```json
{
  "id": "09b9ff6a749bc040",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291570,
  "host_pid": "9e6742732c60:1",
  "hash": "b9c87f90fce46e72d8e09ddcd04ae3c43500c3b82df5741d8022f6bdfd1fa022",
  "cid": "QmV1b9c87f90fce46e72d8e09ddcd04ae3c43500c3b8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291570,
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
      "evaluated_at": 1760291570
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
  "sig": "caa9bb5dc806e9440fc5614066cb98363a25caf8578c9aeb510192f2534a627d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464749166
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 178, 'threshold': 50, 'total_amount': 63476936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 177, 'first_seen': 1760285764, 'matching_hash': '2c72b457e71ecad2'}}}