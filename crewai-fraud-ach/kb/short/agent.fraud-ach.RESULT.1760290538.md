```json
{
  "id": "095e5f21601da656",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290538,
  "host_pid": "9e6742732c60:1",
  "hash": "579232e9a43adb0798e7a8932a29b63ca30a9532a046f1d4f899cb676282a8be",
  "cid": "QmV1579232e9a43adb0798e7a8932a29b63ca30a9532",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290538,
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
      "evaluated_at": 1760290538
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
  "sig": "2ebc70f83f2e8e74013e4b7c4b21d3fc839cdbf6d2f66da2365851d2e280a0f5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025087725
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 57887091, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285763, 'matching_hash': '6f7a0cdb6265bdfa'}}}