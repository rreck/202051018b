```json
{
  "id": "55c5bbda7158c37b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287026,
  "host_pid": "9e6742732c60:1",
  "hash": "02f56892956937642a7da5765094e40d4906669f5e7bd99c0a76852b1da09c26",
  "cid": "QmV102f56892956937642a7da5765094e40d4906669f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287026,
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
      "evaluated_at": 1760287026
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
  "sig": "0c45c4c0f2d23cada556af83dbd8be6306016105a1f04280b67dca6c595adcec"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 14321160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 44, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}