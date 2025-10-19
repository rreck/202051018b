```json
{
  "id": "6e9985b17ad6af6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287559,
  "host_pid": "9e6742732c60:1",
  "hash": "74011300ca3c43324ae7a37baea6a9b4a171d229a6155306316bb97c2b5b178f",
  "cid": "QmV174011300ca3c43324ae7a37baea6a9b4a171d229",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287559,
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
      "evaluated_at": 1760287559
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
  "sig": "f7562145db8c9baaff3fe5bfdd9dd987998754ee61d4f50004427d67f54076d4"
}
```

Fraud detected: duplicate_transaction (score: 81)
Transaction: 044000039834912
Details: {'velocity': {'fraud_detected': True, 'risk_score': 78, 'details': {'transaction_count': 64, 'threshold': 50, 'total_amount': 22281984, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 63, 'first_seen': 1760285765, 'matching_hash': '21095e194860d742'}}}