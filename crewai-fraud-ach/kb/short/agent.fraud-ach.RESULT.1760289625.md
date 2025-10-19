```json
{
  "id": "2581ecb104bf4430",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289625,
  "host_pid": "9e6742732c60:1",
  "hash": "fa7b42bbb192c281ccb376b52fdcd3d400a6bd517b526e5380a1ab79e4225464",
  "cid": "QmV1fa7b42bbb192c281ccb376b52fdcd3d400a6bd51",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289625,
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
      "evaluated_at": 1760289625
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
  "sig": "6d4817a80024bc28b47aaa2154a67199a81a656f5fdfd25fe2a253962136595a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000029386599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 128, 'threshold': 50, 'total_amount': 10761728, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 127, 'first_seen': 1760285765, 'matching_hash': 'b64c8fcbcd38380f'}}}