```json
{
  "id": "009034b9700bd28d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287466,
  "host_pid": "9e6742732c60:1",
  "hash": "39b0fe43c876cc0cbee5e66b92b9f27cf7f9faa79dc2e250f7adb4dc629221d3",
  "cid": "QmV139b0fe43c876cc0cbee5e66b92b9f27cf7f9faa7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287466,
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
      "evaluated_at": 1760287466
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
  "sig": "4986550d463de0e3515f3fa8fd00f4e98c4941182dce7b81e80d91c2837efd97"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 111000027064013
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 18155674, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': '811cb7a859f68158'}}}