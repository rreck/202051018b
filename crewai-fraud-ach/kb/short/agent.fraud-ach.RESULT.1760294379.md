```json
{
  "id": "3a91f8f570ce1282",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294379,
  "host_pid": "9e6742732c60:1",
  "hash": "b2744fc4b67c34135c3842bfff8e960743c5909edd6870fc57e39d953d8d2aae",
  "cid": "QmV1b2744fc4b67c34135c3842bfff8e960743c5909e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294379,
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
      "evaluated_at": 1760294379
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
  "sig": "ebb243ecbdd1f3c4859869a1c859b8c8491116e8d3f31d9ffbc779915b9564f0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247065619
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 94768479, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285763, 'matching_hash': '73a93f9011d99735'}}}