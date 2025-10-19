```json
{
  "id": "6ab095717130633d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292802,
  "host_pid": "9e6742732c60:1",
  "hash": "a6e702ec75adb56c32a29c72c439c73aa803bcca69b11d5d7b8bb6aa294dc909",
  "cid": "QmV1a6e702ec75adb56c32a29c72c439c73aa803bcca",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292802,
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
      "evaluated_at": 1760292802
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
  "sig": "2abbb5025bf4e9860efd4ab88c39126cf0db3e32daa2404da5d7a55c17eb10ac"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245329334
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 205, 'threshold': 50, 'total_amount': 75600310, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 204, 'first_seen': 1760285765, 'matching_hash': 'de3fbc58a94e529a'}}}