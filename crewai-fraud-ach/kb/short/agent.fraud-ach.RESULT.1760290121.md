```json
{
  "id": "d8048acdcaf4e419",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290121,
  "host_pid": "9e6742732c60:1",
  "hash": "5f04479bb192c976be7eda6e729a4e6e89e76eecbb0dd4482902035d7587d4ff",
  "cid": "QmV15f04479bb192c976be7eda6e729a4e6e89e76eec",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290121,
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
      "evaluated_at": 1760290121
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
  "sig": "3c439f9f2603a410bc0dfcedc97813ebc3eb17deadedd304f5ba372c5f0d0cc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026198505
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 66512942, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285764, 'matching_hash': '8ff7ad30241d2e02'}}}