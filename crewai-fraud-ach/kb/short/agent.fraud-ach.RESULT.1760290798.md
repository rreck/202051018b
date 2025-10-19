```json
{
  "id": "eeb63bd4e553ba94",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290798,
  "host_pid": "9e6742732c60:1",
  "hash": "cbe5e492c30609e2d5cf8fbe479adea24551d367ba69823885518ed3daa9f627",
  "cid": "QmV1cbe5e492c30609e2d5cf8fbe479adea24551d367",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290798,
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
      "evaluated_at": 1760290798
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
  "sig": "148118eb58690b9f7f85211f01ec0dd2f0547bea475ddb821c4cdae486b3c8f7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151363741
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 159, 'threshold': 50, 'total_amount': 68913621, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 158, 'first_seen': 1760285765, 'matching_hash': 'ec824383c23ded7d'}}}