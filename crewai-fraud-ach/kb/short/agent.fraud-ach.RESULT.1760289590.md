```json
{
  "id": "622762e2ba61450a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289590,
  "host_pid": "9e6742732c60:1",
  "hash": "2ec4ac092a567a9d7e6073afa0a3df4626363a16667c102c7f9d3724110044c0",
  "cid": "QmV12ec4ac092a567a9d7e6073afa0a3df4626363a16",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289590,
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
      "evaluated_at": 1760289590
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
  "sig": "fdaa7cdde572f3da1ad907605c37ef26800a67722fa74430421a944552a2b5a2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 127, 'threshold': 50, 'total_amount': 40417496, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 126, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}