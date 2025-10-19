```json
{
  "id": "e55ea39dceb3a9f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293307,
  "host_pid": "9e6742732c60:1",
  "hash": "94a48bf4e13bd1e0543fbd916af5f1f0f82a5ee5dbb1d9129701d9d896a8b400",
  "cid": "QmV194a48bf4e13bd1e0543fbd916af5f1f0f82a5ee5",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293307,
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
      "evaluated_at": 1760293307
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
  "sig": "31bbe8d52b198c8ec4ad3820d4b7cb9243cf3d5a72387be852d8319b6fb79105"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464670752
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 90187128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': '207898f44ec5d129'}}}