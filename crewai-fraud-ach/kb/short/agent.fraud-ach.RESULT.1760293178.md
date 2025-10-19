```json
{
  "id": "0e2e567a1c3de88a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293178,
  "host_pid": "9e6742732c60:1",
  "hash": "b4931613ba2c42640c08eb080abc2e2ce73f3e92eef02d6b97f3ec9e5b50cf68",
  "cid": "QmV1b4931613ba2c42640c08eb080abc2e2ce73f3e92",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293178,
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
      "evaluated_at": 1760293178
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
  "sig": "85197415151bbd37d35aca99fbd9524a0a7ec4d972a554da98ed7a19b0744273"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158715464
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 31562553, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '08e14bce24e2b1ea'}}}