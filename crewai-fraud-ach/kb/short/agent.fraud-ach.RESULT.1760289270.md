```json
{
  "id": "21f72893768467dd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289270,
  "host_pid": "9e6742732c60:1",
  "hash": "69b16fbfc50a8e15fd339ebd50fc6140aaeb454add7318d546c7d464042a824b",
  "cid": "QmV169b16fbfc50a8e15fd339ebd50fc6140aaeb454a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289270,
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
      "evaluated_at": 1760289270
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
  "sig": "07a2aed865028b307adc92f8f6a16a4169a834d541ff00ad26c7ee2b3d55c060"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 22560066, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}