```json
{
  "id": "a932ef8b878a89f0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289189,
  "host_pid": "9e6742732c60:1",
  "hash": "3f403552b80f27320f536573ab2429f36979a3d8faed1a90f0eb367625507153",
  "cid": "QmV13f403552b80f27320f536573ab2429f36979a3d8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289189,
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
      "evaluated_at": 1760289189
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
  "sig": "2cb0af63a511499bd4e453090c24b4ff71ca1b0a9d0734491d7ba12d6034dc80"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021412484
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 28527880, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285764, 'matching_hash': 'a5f4ca8ac1007b12'}}}