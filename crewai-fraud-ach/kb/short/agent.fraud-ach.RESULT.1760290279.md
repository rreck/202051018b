```json
{
  "id": "34aca8ee1c13f75e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290279,
  "host_pid": "9e6742732c60:1",
  "hash": "27faf10a7bd38d9bf8ef2a02e082575fbc1994f87e55f85896a695be4d12a1a4",
  "cid": "QmV127faf10a7bd38d9bf8ef2a02e082575fbc1994f8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290279,
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
      "evaluated_at": 1760290279
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
  "sig": "6d3a930b59f6f351d21962d6191a67df15e9295741efa7c63651852df87de725"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020288859
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 146, 'threshold': 50, 'total_amount': 70757586, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 145, 'first_seen': 1760285765, 'matching_hash': '0e6f21190a149d49'}}}