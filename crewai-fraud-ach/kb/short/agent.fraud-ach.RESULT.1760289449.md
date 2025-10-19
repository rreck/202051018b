```json
{
  "id": "aa94cb06269a1bbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289449,
  "host_pid": "9e6742732c60:1",
  "hash": "385ae4d5b27600144362329ccd7ce111dc40c74f8130be585f4124bb1de04aa2",
  "cid": "QmV1385ae4d5b27600144362329ccd7ce111dc40c74f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289449,
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
      "evaluated_at": 1760289449
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
  "sig": "7c813cc4a48c99319073b027f7fa1291e511d5bec5ba6f1d24587590346d6566"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 123, 'threshold': 50, 'total_amount': 39144504, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 122, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}