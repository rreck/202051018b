```json
{
  "id": "03c4ad2484a1a1d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290680,
  "host_pid": "9e6742732c60:1",
  "hash": "659c7389b3e5818c59a918e64c156b16ad1e7856a4a7cc56bdbc9f9e58c1b46a",
  "cid": "QmV1659c7389b3e5818c59a918e64c156b16ad1e7856",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290680,
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
      "evaluated_at": 1760290680
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
  "sig": "f5174e7732dbfe0250f1e5c0089e21e6e70480653014912697a275e0a79818c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 156, 'threshold': 50, 'total_amount': 49646688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 155, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}