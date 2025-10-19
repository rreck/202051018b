```json
{
  "id": "b6a21ba7c70f9466",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290168,
  "host_pid": "9e6742732c60:1",
  "hash": "6efc4b5c4d8aa58d8bb88dfaf6bd85c5ec372dbb0124286ba28aa7e4cfe1f120",
  "cid": "QmV16efc4b5c4d8aa58d8bb88dfaf6bd85c5ec372dbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290168,
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
      "evaluated_at": 1760290168
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
  "sig": "1b274ad4c52757472b8cdf173bbd6c459cc769e3623b7fbaf94c9ff2be2d3b43"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000244797937
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 143, 'threshold': 50, 'total_amount': 56625426, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 142, 'first_seen': 1760285765, 'matching_hash': 'e00995c9aab9b89d'}}}