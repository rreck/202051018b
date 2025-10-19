```json
{
  "id": "184d557bb208accd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294707,
  "host_pid": "9e6742732c60:1",
  "hash": "c34a78ad76ddb8cceb87e0b1a6e0535ffb9ff8e9a06d2bccaa5487fc2c6dbbfd",
  "cid": "QmV1c34a78ad76ddb8cceb87e0b1a6e0535ffb9ff8e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294707,
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
      "evaluated_at": 1760294707
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
  "sig": "8ab24fd8140e08f4656ee89dd5cb051afe8f2badb196819eb77b612939f4dfb6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023973780
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 21325680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285763, 'matching_hash': 'a6cf7acef53d66c2'}}}