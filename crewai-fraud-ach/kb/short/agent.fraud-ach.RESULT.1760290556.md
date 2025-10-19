```json
{
  "id": "2e6659ade9e94bf2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290556,
  "host_pid": "9e6742732c60:1",
  "hash": "b4c18a9497fe83de283bf3f0a8939f1d3570d326c42e2673745e794fe9cef555",
  "cid": "QmV1b4c18a9497fe83de283bf3f0a8939f1d3570d326",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290556,
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
      "evaluated_at": 1760290556
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
  "sig": "598edd453fb4b5aeb9f9397d67d13b4c6281a0d89d972b74047ede22544c512d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248125638
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 153, 'threshold': 50, 'total_amount': 67861467, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 152, 'first_seen': 1760285764, 'matching_hash': '28ad2138639324d3'}}}