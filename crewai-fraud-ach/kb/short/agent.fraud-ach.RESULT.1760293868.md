```json
{
  "id": "3b4f11378fd06639",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293868,
  "host_pid": "9e6742732c60:1",
  "hash": "6e5e38e966e14077d5d5db5f31cc0b4e01742cbcb6a04e4233fc6529568b5717",
  "cid": "QmV16e5e38e966e14077d5d5db5f31cc0b4e01742cbc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293868,
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
      "evaluated_at": 1760293868
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
  "sig": "75228919aec71fecc100eb9a466aedea6933f7d3283456cd8b44785346ee5591"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030199431
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 227, 'threshold': 50, 'total_amount': 109438516, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 226, 'first_seen': 1760285763, 'matching_hash': '86eebb6c1a57e398'}}}